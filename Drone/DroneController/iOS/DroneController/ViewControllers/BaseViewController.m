//
//  BaseViewController.m
//  DroneController
//
//  Created by lucid on 06/03/2019.
//  Copyright © 2019 lucid. All rights reserved.
//

#import "BaseViewController.h"

@interface BaseViewController ()

@end

@implementation BaseViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

#pragma mark - user function
- (void)setTitleBarText:(NSString*)strTitle {
    if(self.navigationController!=nil && strTitle.length > 0) {
        [self setTitle:strTitle];
        self.navigationController.navigationBar.hidden = NO;
    }
    else {
        self.navigationController.navigationBar.hidden = YES;
    }
}
@end
