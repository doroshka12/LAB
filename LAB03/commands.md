2. tree -L 2
3. cd /etc/
4. ls -a
5. ls -lX
6. cd -
mkdir structure
7. cd structure
mkdir 2018
mkdir 2019
mkdir 2020
mkdir 2021
mkdir 2022
mkdir 2023
cd 2018
mkdir files
mkdir pictures
mkdir .passwords
cd -
cd 2019
mkdir files
mkdir pictures
mkdir .passwords
cd -
cd 2020
mkdir files
mkdir pictures
mkdir .passwords
cd -
cd 2021
mkdir files
mkdir pictures
mkdir .passwords
cd -
cd 2022
mkdir files
mkdir pictures
mkdir .passwords
cd-
cd 2023
mkdir files
mkdir pictures
mkdir .passwords
cd-
8. 9. 10. ls 
cd 2018
cd files
touch data md
cd- 
cd pictures
touch picture.png
cd-
cd .passwords
touch .passwords.txt
cd-
cd-
cd 2019
cd files
touch data md
cd- 
cd pictures
touch picture.png
cd-
cd .passwords
touch .passwords.txt
cd-
cd-
cd 2020
cd files
touch data md
cd- 
cd pictures
touch picture.png
cd-
cd .passwords
touch .passwords.txt
cd-
cd-
cd 2021
cd files
touch data md
cd- 
cd pictures
touch picture.png
cd-
cd .passwords
touch .passwords.txt
cd-
cd-
cd 2022
cd files
touch data md
cd- 
cd pictures
touch picture.png
cd-
cd .passwords
touch .passwords.txt
cd-
cd-
cd 2023
cd files
touch data md
cd- 
cd pictures
touch picture.png
cd-
cd .passwords
touch .passwords.txt
cd-
cd-
11. touch -ad "20240101" data.md
12. touch -d "20180610" .passwords.txt
 touch -d "20190610" .passwords.txt
 touch -d "20200610" .passwords.txt
 touch -d "20210610" .passwords.txt
 touch -d "20220610" .passwords.txt
touch -d "20230610" .passwords.txt
13. cp structure/2023 Downloads/2025 -r
14. touch -d "20250610" .passwords.txt
15. cp Downloads/2025 structure -r
16. mv 2025 2024
17. mv picture.png image.png
18. mv structure/2018 Documents/
19. rmdir -p ~/Documents/2024 
20. rm -r ~/Documents/2024
21. cat > ~/structure/2019/files/data.md
jhldkajfhslkajhsdfjh
22. cd structure
cd 2020
cd  files
nano data.md
lkajshbklfjkajsdhf
23. code structure/2021/files/data.md  
24. cat ~/structure/2020/files/data.md > ~/structure/2022/files/data.md
 25. cd structure
 mkdir -p {soft_links,hard_links}
 tree
 26. ln -s /home/doroshkevich/structure/2018/ /home/doroshkevich/structure/soft_links/2018
 ln -s /home/doroshkevich/structure/2019/ /home/doroshkevich/structure/soft_links/2019
 ln -s /home/doroshkevich/structure/2020/ /home/doroshkevich/structure/soft_links/2020
 ln -s /home/doroshkevich/structure/2021/ /home/doroshkevich/structure/soft_links/2021
 ln -s /home/doroshkevich/structure/2022/ /home/doroshkevich/structure/soft_links/2022
 ln -s /home/doroshkevich/structure/2023/ /home/doroshkevich/structure/soft_links/2023
 ls -li soft_links
 27. ln ~/structure/2020/files/data.md ~/structure/hard_links/data
 cat ~/structure/hard_links/data
 ln /home/doroshkevich/structure/2021/.passwords/.passwords.txt /home/doroshkevich/structure/hard_links/.password
 28. mkdir -p ~/structure/archives
30. mv ~/Downloads/image.jpg ~/structure/archives 
31. tar -c -f ~/structure/archives/image.tar ~/structure/archives/image.jpg
tar -c -f ~/structure/archives/image.tar.gz ~/structure/archives/image.jpg
tar -c -f ~/structure/archives/image.tar.bz2 ~/structure/archives/image.jpg
32. zip -r -e structure.zip structure
