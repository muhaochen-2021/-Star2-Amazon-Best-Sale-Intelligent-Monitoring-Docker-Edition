# Amazon Best Sale Intelligent Monitoring  (Docker Edition) 

Amazon Best Sale Intelligent Monitoring is a back-end program based on Flask, using python, html+css+js, echarts, LSTM, wordcloud, which is deployed on Docker. This Program can grasp the real-time data each hour,including the name, sale, price, score and comments of best sale products from the amazon, and generating the visulization of the tendency of products. Saler can make intelligent marketing strategy.

## Programming and Enviornment
Python, flask, html+css+js, echarts and Docker.

## File Structure
- static
- templates
- venv1
- app.py
- docker-compose.yaml
- Dockerfile
- Dockerfile2
- get_amz_data.py
- l1_page.py
- l2_page.py
- readme.md
- requirements.txt
- requirements2.txt


## Run
Because all the steps and actions are written in the docker-compose.yml, 
we just open the Windows PowerShell, and:
    Run docker-compose up
    
Then, we would get the results we want:
    the 4 images are installed...
    the 4 containers are installed...
    the get_amz_data.py and app.py are running simultaneously and never stop, unless stop manully...

Then, we should type localhost:5000/ to request the URL. 
