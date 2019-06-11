create table thumb_item
(
  id VARCHAR(32) PRIMARY KEY ,
  name VARCHAR(50),
  img_url VARCHAR(200),
  info_url VARCHAR(200),
  width VARCHAR(10),
  height VARCHAR(10)
);

CREATE TABLE item_info
(
  uid VARCHAR(32) NOT NULL ,
  img_url VARCHAR(200)
);