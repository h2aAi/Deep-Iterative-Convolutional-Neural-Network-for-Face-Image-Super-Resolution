DIC16(
  (conv_in): Sequential(
    (0): Conv2d(3, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): PReLU(num_parameters=1)
  )
  (conv_in_2): Sequential(
    (0): Conv2d(192, 768, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): PReLU(num_parameters=1)
  )
  (feat_in): PixelShuffle(upscale_factor=4)
  (first_block): FeedbackBlockCustom(
    (compress_in): Sequential(
      (0): Conv2d(48, 48, kernel_size=(1, 1), stride=(1, 1))
      (1): PReLU(num_parameters=1)
    )
    (upBlocks): ModuleList(
      (0): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (5): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
    )
    (downBlocks): ModuleList(
      (0): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (5): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
    )
    (uptranBlocks): ModuleList(
      (0): Sequential(
        (0): Conv2d(96, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): Conv2d(144, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): Conv2d(192, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): Conv2d(240, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): Conv2d(288, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
    )
    (downtranBlocks): ModuleList(
      (0): Sequential(
        (0): Conv2d(96, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): Conv2d(144, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): Conv2d(192, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): Conv2d(240, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): Conv2d(288, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
    )
    (compress_out): Sequential(
      (0): Conv2d(288, 48, kernel_size=(1, 1), stride=(1, 1))
      (1): PReLU(num_parameters=1)
    )
  )
  (block): FeedbackBlockHeatmapAttention(
    (compress_in): Sequential(
      (0): Conv2d(96, 48, kernel_size=(1, 1), stride=(1, 1))
      (1): PReLU(num_parameters=1)
    )
    (upBlocks): ModuleList(
      (0): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (5): Sequential(
        (0): ConvTranspose2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
    )
    (downBlocks): ModuleList(
      (0): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
      (5): Sequential(
        (0): Conv2d(48, 48, kernel_size=(12, 12), stride=(8, 8), padding=(2, 2))
        (1): PReLU(num_parameters=1)
      )
    )
    (uptranBlocks): ModuleList(
      (0): Sequential(
        (0): Conv2d(96, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): Conv2d(144, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): Conv2d(192, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): Conv2d(240, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): Conv2d(288, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
    )
    (downtranBlocks): ModuleList(
      (0): Sequential(
        (0): Conv2d(96, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (1): Sequential(
        (0): Conv2d(144, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (2): Sequential(
        (0): Conv2d(192, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (3): Sequential(
        (0): Conv2d(240, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
      (4): Sequential(
        (0): Conv2d(288, 48, kernel_size=(1, 1), stride=(1, 1))
        (1): PReLU(num_parameters=1)
      )
    )
    (compress_out): Sequential(
      (0): Conv2d(288, 48, kernel_size=(1, 1), stride=(1, 1))
      (1): PReLU(num_parameters=1)
    )
    (fusion_block): FeatureHeatmapFusingBlock(
      (conv_in): Sequential(
        (0): Conv2d(48, 240, kernel_size=(1, 1), stride=(1, 1))
        (1): LeakyReLU(negative_slope=0.2, inplace=True)
      )
      (resnet): Sequential(
        (0): ResBlock(
          (res): Sequential(
            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
            (1): LeakyReLU(negative_slope=0.2, inplace=True)
            (2): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
          )
        )
        (1): ResBlock(
          (res): Sequential(
            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
            (1): LeakyReLU(negative_slope=0.2, inplace=True)
            (2): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
          )
        )
        (2): ResBlock(
          (res): Sequential(
            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
            (1): LeakyReLU(negative_slope=0.2, inplace=True)
            (2): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
          )
        )
        (3): ResBlock(
          (res): Sequential(
            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
            (1): LeakyReLU(negative_slope=0.2, inplace=True)
            (2): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
          )
        )
        (4): ResBlock(
          (res): Sequential(
            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
            (1): LeakyReLU(negative_slope=0.2, inplace=True)
            (2): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
          )
        )
        (5): ResBlock(
          (res): Sequential(
            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
            (1): LeakyReLU(negative_slope=0.2, inplace=True)
            (2): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
          )
        )
        (6): ResBlock(
          (res): Sequential(
            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
            (1): LeakyReLU(negative_slope=0.2, inplace=True)
            (2): Conv2d(240, 240, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=5)
          )
        )
      )
    )
  )
  (out): Sequential(
    (0): ConvTranspose2d(48, 48, kernel_size=(8, 8), stride=(4, 4), padding=(2, 2))
    (1): PReLU(num_parameters=1)
  )
  (conv_out): Sequential(
    (0): Conv2d(48, 3, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
  )
  (HG): FeedbackHourGlass(
    (pre_conv_block): Sequential(
      (0): Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3))
      (1): ReLU(inplace=True)
      (2): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(64, 128, kernel_size=(1, 1), stride=(1, 1))
        )
        (skip_layer): Conv2d(64, 128, kernel_size=(1, 1), stride=(1, 1))
      )
      (3): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
      (4): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(128, 64, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(64, 128, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (5): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(128, 128, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(128, 256, kernel_size=(1, 1), stride=(1, 1))
        )
        (skip_layer): Conv2d(128, 256, kernel_size=(1, 1), stride=(1, 1))
      )
    )
    (compress_in): Conv2d(512, 512, kernel_size=(1, 1), stride=(1, 1))
    (hg): HourGlass(
      (res4_1): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (pool4_1): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
      (res4_2): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res3_1): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (pool3_1): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
      (res3_2): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res2_1): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (pool2_1): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
      (res2_2): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res1_1): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (pool1_1): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
      (res1_2): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res_center): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res1_3): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res2_3): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res3_3): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (res4_3): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(512, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(256, 512, kernel_size=(1, 1), stride=(1, 1))
        )
      )
    )
    (hg_conv_out): Sequential(
      (0): ResidualBlock(
        (conv_block): Sequential(
          (0): Conv2d(256, 128, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
          (2): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
          (3): Conv2d(128, 256, kernel_size=(1, 1), stride=(1, 1))
        )
      )
      (1): Lin(
        (conv_block): Sequential(
          (0): Conv2d(256, 256, kernel_size=(1, 1), stride=(1, 1))
          (1): ReLU(inplace=True)
        )
      )
      (2): Conv2d(256, 68, kernel_size=(1, 1), stride=(1, 1))
    )
  )
)
Network structure: [DataParallel - DIC16], with parameters: [23,131,722]
