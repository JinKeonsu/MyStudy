//
//  MainViewController.m
//  DroneController
//
//  Created by lucid on 06/03/2019.
//  Copyright © 2019 lucid. All rights reserved.
//

#import "MainViewController.h"
#import "MapViewController.h"

@interface MainViewController ()

@end

@implementation MainViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    [self setTitleBarText:@"Drone Controller"];
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/
- (IBAction)mapButtonClicked:(id)sender {
    UIStoryboard *sb = [UIStoryboard storyboardWithName:@"Main" bundle:nil];
    MapViewController *vc = [sb instantiateViewControllerWithIdentifier:@"MapVC"];
    [self.navigationController pushViewController:vc animated:YES];
}

@end
