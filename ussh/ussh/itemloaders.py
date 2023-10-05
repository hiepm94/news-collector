from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class ChocolateProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    url_in = MapCompose(lambda x: 'https://ussh.vnu.edu.vn' + x )