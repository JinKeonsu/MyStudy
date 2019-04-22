//
//  ViewController.m
//  BlueMan
//
//  Created by lucid on 26/03/2019.
//  Copyright © 2019 lucid. All rights reserved.
//

#import "ViewController.h"



#define BLUNO_TRANSFER_SERVICE_UUID         @"0xDFB0"
#define BLUNO_TRANSFER_CHARACTERISTIC_UUID  @"0xDFB2"

@interface ViewController ()
{
    NSMutableArray  *listArray;
}
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.

    _centralManager = [[CBCentralManager alloc] initWithDelegate:self queue:nil options:nil];
    listArray = [[NSMutableArray alloc]init];
}

- (IBAction)btnScanClicked:(id)sender {

}

- (void)initList {

}

#pragma mark - tableView
- (NSInteger) numberOfSectionsInTableView:(UITableView *)tableView {
    return 1;
}

- (NSInteger)tableView:(UITableView *)table numberOfRowsInSection:(NSInteger)section;
{
    return [listArray count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath;
{
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"listCell"];
    if (cell==nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"listCell"];
        cell.selectionStyle = UITableViewCellSelectionStyleBlue;
    }

    cell.textLabel.text = @"fjdalkj";

    return cell;
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath;
{
    if (tableView == self.bleList) {


        [tableView deselectRowAtIndexPath:indexPath animated:YES];
    }
}

- (IBAction)buttonClicked:(id)sender {
    [self showFlowerToggle:@"2"];
}

- (void)showFlowerToggle:(NSString*)sOption
{
    static int nCount = 1;

    if(nCount>5) return;

    UIImage *imgOff = [UIImage imageNamed:@"66"];
    UIImage *imgON= ([sOption isEqualToString:@"1"]) ? [UIImage imageNamed:@"67"] :[UIImage imageNamed:@"68"];
    [UIView transitionWithView:self.iconImage
                      duration:1.f
                       options:UIViewAnimationOptionTransitionCrossDissolve
                    animations:^{
                        self.iconImage.image = imgON;
                    } completion:^(BOOL finished){
                        [UIView transitionWithView:self.iconImage
                                          duration:1.f
                                           options:UIViewAnimationOptionTransitionCrossDissolve
                                        animations:^{
                                            self.iconImage.image = imgOff;
                                        } completion:^(BOOL finished){
                                            nCount++;
                                            [self performSelector:@selector(showFlowerToggle:) withObject:sOption];
                                        }
                         ];
                    }
     ];
}



#pragma mark - CB
// https://www.raywenderlich.com/231-core-bluetooth-tutorial-for-ios-heart-rate-monitor
// https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/CoreBluetoothOverview/CoreBluetoothOverview.html#//apple_ref/doc/uid/TP40013257-CH2-SW1
//https://www.invasivecode.com/weblog/core-bluetooth-for-ios-6-core-bluetooth-was/
- (void)centralManagerDidUpdateState:(CBCentralManager *)central
{
    // You should test all scenarios
    if (central.state == CBCentralManagerStatePoweredOff) {
        //msgbox 'turn on bluetooth'
        return;
    }

    if (central.state == CBCentralManagerStatePoweredOn) {
        // Scan for devices
        [_centralManager scanForPeripheralsWithServices:nil options:nil];
//        [_centralManager scanForPeripheralsWithServices:@[[CBUUID UUIDWithString:BLUNO_TRANSFER_SERVICE_UUID]] options:@{ CBCentralManagerScanOptionAllowDuplicatesKey : @YES }];
    }
}

- (void)centralManager:(CBCentralManager *)central didDiscoverPeripheral:(CBPeripheral *)peripheral advertisementData:(NSDictionary *)advertisementData RSSI:(NSNumber *)RSSI {

    NSLog(@"Discovered %@ at %@", peripheral.name, RSSI);
    if (_discoveredPeripheral != peripheral) {
        // Save a local copy of the peripheral, so CoreBluetooth doesn't get rid of it
        _discoveredPeripheral = peripheral;
        // And connect
        NSLog(@"Connecting to peripheral %@", peripheral);
        [_centralManager connectPeripheral:peripheral options:nil];

        // then stop scanning for peripherals
        [_centralManager stopScan];
        NSLog(@"Scanning stopped");
    }
}

- (void)centralManager:(CBCentralManager *)central didFailToConnectPeripheral:(CBPeripheral *)peripheral error:(NSError *)error {
    NSLog(@"Failed to connect");
    [self cleanup];
}

- (void)cleanup {
    // See if we are subscribed to a characteristic on the peripheral
    if (_discoveredPeripheral.services != nil) {
        for (CBService *service in _discoveredPeripheral.services) {
            if (service.characteristics != nil) {
                for (CBCharacteristic *characteristic in service.characteristics) {
                    if ([characteristic.UUID isEqual:[CBUUID UUIDWithString:BLUNO_TRANSFER_CHARACTERISTIC_UUID]]) {
                        if (characteristic.isNotifying) {
                            [_discoveredPeripheral setNotifyValue:NO forCharacteristic:characteristic];
                            return;
                        }
                    }
                }
            }
        }
    }
    [_centralManager cancelPeripheralConnection:_discoveredPeripheral];
}

- (void)centralManager:(CBCentralManager *)central didConnectPeripheral:(CBPeripheral *)peripheral {
    NSLog(@"Connected");
    [_centralManager stopScan];
    NSLog(@"Scanning stopped");

//    [_data setLength:0];
    peripheral.delegate = self;
    [peripheral discoverServices:@[[CBUUID UUIDWithString:BLUNO_TRANSFER_SERVICE_UUID]]];
}

- (void)peripheral:(CBPeripheral *)peripheral didDiscoverServices:(NSError *)error {
    if (error) {
        [self cleanup];
        return;
    }
    for (CBService *service in peripheral.services) {
        [peripheral discoverCharacteristics:@[[CBUUID UUIDWithString:BLUNO_TRANSFER_CHARACTERISTIC_UUID]] forService:service];
    }
    // Discover other characteristics
}

- (void)peripheral:(CBPeripheral *)peripheral didDiscoverCharacteristicsForService:(CBService *)service error:(NSError *)error {
    if (error) {
        [self cleanup];
        return;
    }
    for (CBCharacteristic *characteristic in service.characteristics) {
        if ([characteristic.UUID isEqual:[CBUUID UUIDWithString:BLUNO_TRANSFER_CHARACTERISTIC_UUID]]) {
            [peripheral setNotifyValue:YES forCharacteristic:characteristic];
        }
    }
}

- (void)peripheral:(CBPeripheral *)peripheral didUpdateValueForCharacteristic:(CBCharacteristic *)characteristic error:(NSError *)error {
    if (error) {
        NSLog(@"Error");
        return;
    }
    NSString *stringFromData = [[NSString alloc] initWithData:characteristic.value encoding:NSUTF8StringEncoding];
    // Have we got everything we need?
    if ([stringFromData isEqualToString:@"EOM"]) {
        //[_textview setText:[[NSString alloc] initWithData:self.data encoding:NSUTF8StringEncoding]];
        [peripheral setNotifyValue:NO forCharacteristic:characteristic];
        [_centralManager cancelPeripheralConnection:peripheral];
    }
//    [_data appendData:characteristic.value];
}

- (void)peripheral:(CBPeripheral *)peripheral didUpdateNotificationStateForCharacteristic:(CBCharacteristic *)characteristic error:(NSError *)error {
    if (![characteristic.UUID isEqual:[CBUUID UUIDWithString:BLUNO_TRANSFER_CHARACTERISTIC_UUID]]) {
        return;
    }
    if (characteristic.isNotifying) {
        NSLog(@"Notification began on %@", characteristic);
    } else {
        // Notification has stopped
        [_centralManager cancelPeripheralConnection:peripheral];
    }
}

- (void)centralManager:(CBCentralManager *)central didDisconnectPeripheral:(CBPeripheral *)peripheral error:(NSError *)error {
    _discoveredPeripheral = nil;
    [_centralManager scanForPeripheralsWithServices:@[[CBUUID UUIDWithString:BLUNO_TRANSFER_SERVICE_UUID]] options:@{ CBCentralManagerScanOptionAllowDuplicatesKey : @YES }];
}

@end
