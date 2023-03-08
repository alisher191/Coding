import speedtest
sp_t = speedtest.Speedtest()

download_speed = int(sp_t.download()/1000000)
upload_speed = int(sp_t.upload()/1000000)
ping = sp_t.results.ping

print(f'Скорость скачивания: {download_speed} Мбит/с')
print(f'Скорость загрузки: {upload_speed} Мбит/с')
print(f"Пинг: {ping}")
