CREATE TABLE "bus_details"(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "Departure_time" DATETIME NOT NULL,
    "Arrival_time" DATETIME NOT NULL,
    "From" TEXT NOT NULL,
    "To" TEXT NOT NULL,
    "Bus_number" INTEGER NOT NULL
);

CREATE TABLE "customer"(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "Name" TEXT NOT NULL,
    "Contact" INTEGER NOT NULL,
    "DOB" INTEGER NOT NULL
);

CREATE TABLE "booking"(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "customer_id" INTEGER,
    "bus_id" INTEGER,
    "Payment_status" BOOLEAN,
    CONSTRAINT LINK_CUSTOMER  FOREIGN KEY("customer_id") REFERENCES customer('id'),
    CONSTRAINT LINK_BUS  FOREIGN KEY("bus_id") REFERENCES bus_details('id') 
    
);