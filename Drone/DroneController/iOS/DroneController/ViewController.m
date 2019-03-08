//
//  ViewController.m
//  DroneController
//
//  Created by lucid on 06/03/2019.
//  Copyright © 2019 lucid. All rights reserved.
//

#import "ViewController.h"
#import "MainViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    [self setTitleBarText:@""];
    
    [self performSelector:@selector(loadMainViewController) withObject:nil afterDelay:2.f];
}

#pragma mark - load main view
- (void)loadMainViewController {
    UIStoryboard *sb = [UIStoryboard storyboardWithName:@"Main" bundle:nil];
    MainViewController *vc = [sb instantiateViewControllerWithIdentifier:@"MainVC"];
    [self.navigationController pushViewController:vc animated:YES];
}


@end
