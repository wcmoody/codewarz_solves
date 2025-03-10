# Retro_Dave_Part_Deux

# Description

<p>Retro Dave is coming off of his Tab induced sugar-high and realized that his Game Boy and Game Boy color games are also separated by system and alphabetized, not cool mom... He likes to put the two collections into one and still sort them by release date and then by title, indicate which system they belong to in your output. Be sure to remove all titles that do not have a release date. Sit down and take a minute to crank out a quick script to help Retro Dave fix his collection while he sits in the corner and moves from Tab to his cache of Bawls drinks (how much punishment can his heart take?). Follow the format in the provided output.<br/><br/>
Example files found <a href="GameBoyShort.csv">here</a> and <a href="/static/downloads/GameBoyColorShort.csv">here</a></p>

## Sample Input:

```
$ ./break_retro_deux.py GameBoyShort.csv GameBoyColorShort.csv
```
## Expected Output:

```
$ ./break_retro_deux.py GameBoyShort.csv GameBoyColorShort.csv 
Castlevania: T~ 1989-12-01       Game Boy
    Pit-Fighter 1992-06-01       Game Boy
Jeep Jamboree:~ 1992-07-01       Game Boy
   Looney Tunes 1992-10-01       Game Boy
Rocky and Bull~ 1992-10-01       Game Boy
Star Trek: The~ 1993-06-01       Game Boy
Muhammad Ali H~ 1993-07-01       Game Boy
World Heroes 2~ 1995-08-01       Game Boy
Battle Zone/Su~ 1996-10-01       Game Boy
 10 Pin Bowling 1999-08-01 Game Boy Color
Gex 3: Deep Po~ 1999-12-01       Game Boy
  Tonka Raceway 1999-12-01 Game Boy Color
Tiger Woods Go~ 2000-01-01       Game Boy
           1942 2000-05-01       Game Boy
Micro Machines~ 2000-11-01 Game Boy Color
      Road Rash 2000-11-01 Game Boy Color
Dragon Warrior~ 2001-09-01       Game Boy
Cubix: Robots ~ 2001-11-01 Game Boy Color
Harry Potter a~ 2001-11-01 Game Boy Color


```
## Expected SHA1 Hash:

```
c6ed968afc88c164d3ad08bbb75dc49b41c254ed
```
