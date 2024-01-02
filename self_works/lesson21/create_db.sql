create role vlone300 nocreatedb createrole login superuser;
alter user vlone300 with password 'pass';
create database user_from_another_site owner vlone300 encoding 'utf-8';