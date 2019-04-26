//
//  ArcheryTargetImageView.h
//  TempTest
//
//  Created by lucid on 26/04/2019.
//  Copyright © 2019 lucid. All rights reserved.
//

#import <UIKit/UIKit.h>

NS_ASSUME_NONNULL_BEGIN

@interface ArcheryTargetImageView : UIImageView {
    BOOL    isFirstShoot;
}

@property (nonatomic, assign)   NSInteger   toggleCount;
@property (nonatomic, retain)   NSString    *normalImageName;
@property (nonatomic, retain)   NSString    *shoot1ImageName;
@property (nonatomic, retain)   NSString    *shoot2ImageName;


- (void)showImageToggle:(NSString*)sOption;


@end

NS_ASSUME_NONNULL_END
