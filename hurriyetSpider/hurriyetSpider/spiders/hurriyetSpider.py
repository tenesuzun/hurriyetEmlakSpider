import scrapy

class hurriyetSpider(scrapy.Spider):
    name = "hurriyetSpider"

    start_urls = ["https://www.hurriyetemlak.com/basaksehir-satilik?districts=basaksehir-bahcesehir-1-kisim,basaksehir-bahcesehir-2-kisim,basaksehir-basak,basaksehir-basaksehir-mah,basaksehir-altinsehir,guvercintepe,basaksehir-kayabasi,basaksehir-sahintepe,basaksehir-ziyagokalp-mah,basaksehir-ikitelli-osb,basaksehir-samlar&page=%s" % page for page in range(1,26)]

    def parse(self, response):
        ilan_tarihi_list = response.xpath('//*[@class="listingView type-1000010100"]/div[1]/div[2]/div[1]/div[1]/div[2]/span/text()').getall()
        fiyat_list = response.xpath('//*[@class="listingView type-1000010100"]//div//div[2]//div[1]//div[1]/text()').getall()
        tasinmaz_tipi = response.xpath("//*[@class='left']/span[2]/text()").getall()
        aciklama_list = response.xpath('//*[@class="list-view-header"]/span/text()').getall()
        adres_list = response.xpath('//*[@class="list-view-location"]//span/text()').getall()
        m2_list = response.xpath('//*[@class="celly squareMeter list-view-size"]/span/span/span/text()').getall()
        oda_list = response.xpath('//*[@class="celly houseRoomCount"]/span/span/text()').getall()
        yas_list = response.xpath('//*[@class="celly buildingAge"]/span/text()').getall()
        kat_list = response.xpath('//*[@class="celly floortype"]/text()').getall()

        fiyat_list = fiyat_list[::7]
        
        adres = []

        for item in range(0,len(adres_list)-1, 2):
            adres.append(adres_list[item]+' '+adres_list[item+1])

        for i in range(len(ilan_tarihi_list)):
            fiyat_list[i] = fiyat_list[i].strip()
            ilan_tarihi_list[i] = ilan_tarihi_list[i].strip()
            adres[i] = adres[i].strip()
            aciklama_list[i] = aciklama_list[i].strip()
            tasinmaz_tipi[i] = tasinmaz_tipi[i].strip()
            m2_list[i] = m2_list[i].strip()
            oda_list[i] = oda_list[i].strip()
            yas_list[i] = yas_list[i].strip()
            kat_list[i] = kat_list[i].strip()

            yield {
            "Taşınmaz Tipi": tasinmaz_tipi[i],
            "Açıklama" : aciklama_list[i],
            "Oda Sayısı" : oda_list[i],
            "Metre Karesi": m2_list[i],
            "Yaş" : yas_list[i],
            "Kat" : kat_list[i],
            "Fiyat" : fiyat_list[i],
            "Adres": adres[i],
            "İlan Tarihi" : ilan_tarihi_list[i]
            }