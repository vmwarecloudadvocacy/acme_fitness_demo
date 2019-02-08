## Steps for deployment with docker-compose

1. Run the following command

```
sudo docker-compose pull && docker-compose up 

```

2. This should pull the images from gcr.io/vmwarecloudadvocacy container repository and run the images

3. Access the application on default port **3000** at ```http://{MACHINE_IP}:3000/

4. To stop the application, use the following command
   
   ``` sudo docker-compose stop ```
   
5. To completely remove all containers, use the following command

    ``` sudo docker-compose down --remove-orphans ```

**IMPORTANT** 

While running steps 1 and 4 make sure you are in the same directory as the docker-compose.yml file. 

## Additional Info

1. Make sure no other container is running on the ports mapped by this application. You might notice that containers will fail to start if such other containers exists. Kill those containers before deploying this application.
