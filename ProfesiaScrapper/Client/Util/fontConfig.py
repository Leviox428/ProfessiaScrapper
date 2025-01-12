class FontConfig:
    fontFamily = "Inter"
    defaultSize = 12

    @staticmethod
    def GetFont(size=None, underlined=False):
        if size is None:
            size = FontConfig.defaultSize
        if underlined:
            return (FontConfig.fontFamily, size, "underline")
        else:
            return (FontConfig.fontFamily, size)
    