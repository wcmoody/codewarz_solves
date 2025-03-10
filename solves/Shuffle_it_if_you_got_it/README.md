# Shuffle_it_if_you_got_it

# Description

<p>The path to the input file will be passed into your program as a command line argument when your program is called.<br/><br/>
You've been put in charge of reorganizing the inventory at Acme, Inc. AI has factories at
various sites around the country, each site manufacturing different sets of products. Currently, each site has all of their products stored in a row of warehouses, with each warehouse storing one type of product. Your idea is to move these products around so that the warehouses store the items in alphabetical order. Management likes your idea but is concerned about the cost of moving all of the products. The farther a product has to be moved, the more it costs, so before committing to any re-ordering they would like to know the total length that all products have to be moved at any given site.
</p>

## Sample Input:

```
$ cat /path/to/somefile.txt
xylophones q-tips zeppelins jumpropes

partridges turtledoves frenchhens callingbirds goldenrings geese swans milkers dancers leapers pipers drummers
```
## Expected Output:

```
$ ./shuffle_it_if_you_got_it_solve.py /path/to/somefile.txt
6

48
```
## Expected SHA1 Hash:

```
444120cdcae7863b1ec4e491c816a33333bf3917
```
