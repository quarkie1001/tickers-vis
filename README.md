Docker-Tickers-Vis
---
This repository shows an example of creating a simple prototype of ticker-generating service with a 
realtime graph-building feature. The basis of the implementation is visualization by Plotly Dash, 
and Redis storafe with TimeSeries module for rapid data saving and fetching.

This branch version contains 3 microservice version. It uses Websocker-server that generates tickers values and send it 
over Websocket to Redis storage.

Installation
---
To start a demonstration just start a docker-compose container with:
```docker-compose up```

Ru 
---
Этот репозиторий хранит прототип сервиса по ежесекундной генерации цен 100 искусственных торговых инструментов 
и веб-сервиса их визуализации.
В качестве основы реализации сервиса генерации было выбрано Redis-хранилище с модулем TimeSeries, 
как оптимально подходящее для хранения такого рода данных (временные ряды цен). 
В качестве основы веб-сервиса визуализации был выбран Plotly Dash. 

В этой версии используется схема с использование вебсокетов: 
микросервис генерации цен (продюсер) совмещен с вебсокет-сервером, микросервис хранения данных(консюмер) совмещен с вебсокет-клиентом.

