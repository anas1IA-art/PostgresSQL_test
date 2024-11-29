## setup Docker with PostgreSQL (database)

# Define containers

   - Create docker-compose.yaml file
   - Add the following content
   - Save the file

## Services

### 1. **pgdatabase**
This service runs the PostgreSQL database.

- **Image**: `postgres:13`
- **Environment Variables**:
  - `POSTGRES_USER=root`: The username for PostgreSQL.
  - `POSTGRES_PASSWORD=root`: The password for the PostgreSQL user.
  - `POSTGRES_DB=my_test_db`: The name of the database to be created on startup.
- **Volumes**: 
  - `./my_test_db_postgres_data:/var/lib/postgresql/data`: Maps the local directory `my_test_db_postgres_data` to the PostgreSQL data directory to persist database data.
- **Ports**:
  - `5432:5432`: Exposes PostgreSQL on port `5432`.

### 2. **pgadmin**
This service runs pgAdmin, a web-based PostgreSQL management tool.

- **Image**: `dpage/pgadmin4`
- **Environment Variables**:
  - `PGADMIN_DEFAULT_EMAIL=admin@admin.com`: The default email for logging into pgAdmin.
  - `PGADMIN_DEFAULT_PASSWORD=root`: The password for the pgAdmin user.
- **Volumes**:
  - `pgadmin_data:/var/lib/pgadmin/data`: Stores pgAdmin data persistently.
- **Ports**:
  - `8080:80`: Exposes pgAdmin on port `8080`. You can access pgAdmin in your browser at `http://localhost:8080`.

## Volumes

- **pgadmin_data**: This volume stores pgAdmin's data persistently, ensuring that pgAdmin's settings and user data are not lost when the container is restarted.

## How to Run

1. Ensure you have Docker and Docker Compose installed.
2. Clone or download this repository.
3. Navigate to the project directory and run the following command to start the containers:

   ```bash
   docker-compose up -d

## Connect to PostgreSQL via pgAdmin

Both containers need to be connected to the same network in order for pgAdmin to connect to the PostgreSQL DB.

1. **Go to your browser and navigate to** `http://localhost:8080/`.
2. **pgAdmin should open.** If you encounter any issues, such as the previous container output still showing up, try clearing your browser’s cookies/history by pressing `CTRL + SHIFT + DEL`, or open it in a private browser tab.
3. **Login** using the credentials from the Docker Compose file:
   - **Email**: `admin@admin.com`
   - **Password**: `root`
4. **On pgAdmin**, go to `Object` -> `Register` -> `Server`.
5. **Give it a name**, such as `test_pg`.
6. **Go to the Connection tab**:
   - **Host name/address**: Set this to either `pgdatabase` or `host.docker.internal`.
   - **Port**: `5432`
   - **Username**: `root`
   - **Password**: `root`
7. After entering the details, click **Save** to connect.

- for more informations :

https://github.com/techwithcosta/techwithcosta-yt/blob/main/My%20Dev%20Setup%20For%20Data%20%26%20AI%20(2024)/My%20Dev%20Setup%20For%20Data%20%26%20AI%20(2024).md