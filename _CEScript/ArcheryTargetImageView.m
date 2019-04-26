//
//  ArcheryTargetImageView.m
//  TempTest
//
//  Created by lucid on 26/04/2019.
//  Copyright © 2019 lucid. All rights reserved.
//

#import "ArcheryTargetImageView.h"


#define FIRST_SHOOT         @"1ST"
#define SECOND_SHOOT        @"2ND"
#define TOGGLE_COUNT        20
#define TOGGLE_DURATION     0.5f //1.f


@implementation ArcheryTargetImageView

/*
// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect {
    // Drawing code
}
*/

- (void)showImageToggle:(NSString*)sOption
{
    self.toggleCount = 0;
    
    if ([sOption isEqualToString:FIRST_SHOOT]) {
        isFirstShoot = YES;
    }
    else {
        isFirstShoot = NO;
    }
    
    NSTimer *t = [NSTimer scheduledTimerWithTimeInterval: TOGGLE_DURATION
                                                  target: self
                                                selector:@selector(onTick:)
                                                userInfo: nil repeats:YES];
    NSRunLoop *runner = [NSRunLoop currentRunLoop];
    [runner addTimer:t forMode: NSDefaultRunLoopMode];

//    dispatch_async(dispatch_get_main_queue(), ^{
//        [self toggleImages:sOption];
//    });
}

- (void)onTick:(NSTimer *)timer
{
    if (self.toggleCount >= TOGGLE_COUNT) {
        [timer invalidate];
        self.toggleCount = 0;
        self.image = [UIImage imageNamed:self.normalImageName];
        return;
    }
    else {
        self.toggleCount++;
        NSLog(@"onTick else. %d", (int)self.toggleCount);
        
        if (self.toggleCount % 2 == 1) {
            NSString *strImageName = (isFirstShoot) ? self.shoot1ImageName: self.shoot2ImageName;
            self.image = [UIImage imageNamed:strImageName];
        }
        else {
            self.image = [UIImage imageNamed:self.normalImageName];
        }
    }
}

- (void)toggleImages:(NSString*)sOption
{
    if (self.toggleCount >= TOGGLE_COUNT) {
        self.toggleCount = 0;
        self.image = [UIImage imageNamed:self.normalImageName];
        return;
    }
    
    UIImage *imgOff = [UIImage imageNamed:self.normalImageName];
    UIImage *imgON= ([sOption isEqualToString:FIRST_SHOOT]) ? [UIImage imageNamed:self.shoot1ImageName] :[UIImage imageNamed:self.shoot2ImageName];
    [UIView transitionWithView:self
                      duration:TOGGLE_DURATION
                       options:UIViewAnimationOptionTransitionCrossDissolve
                    animations:^{
                        self.image = imgON;
                    } completion:^(BOOL finished){
                        [UIView transitionWithView:self
                                          duration:TOGGLE_DURATION
                                           options:UIViewAnimationOptionTransitionCrossDissolve
                                        animations:^{
                                            self.image = imgOff;
                                        } completion:^(BOOL finished){
                                            self.toggleCount++;
                                            [self performSelector:@selector(showImageToggle:) withObject:sOption];
                                        }
                         ];
                    }
     ];
}

@end
