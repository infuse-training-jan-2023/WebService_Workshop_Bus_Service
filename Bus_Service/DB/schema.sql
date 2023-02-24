CREATE TABLE "bus_details"(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "departure_time" DATETIME NOT NULL,
    "arrival_time" DATETIME NOT NULL,
    "beginning" TEXT NOT NULL,
    "destination" TEXT NOT NULL,
    "bus_number" INTEGER NOT NULL
);


CREATE TABLE "customer"(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "contact" INTEGER NOT NULL,
    "dob" INTEGER NOT NULL
);


CREATE TABLE "booking"(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "customer_id" INTEGER,
    "bus_id" INTEGER,
    "payment_status" BOOLEAN,
    CONSTRAINT LINK_CUSTOMER  FOREIGN KEY("customer_id") REFERENCES customer('id'),
    CONSTRAINT LINK_BUS  FOREIGN KEY("bus_id") REFERENCES bus_details('id') 
    
);

