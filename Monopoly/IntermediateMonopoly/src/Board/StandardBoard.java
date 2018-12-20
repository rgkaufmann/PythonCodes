package Board;

import Players.Player;

public class StandardBoard {
	
	String[] ChanceCards = {"Advance to Go", "Advance to Illinois Ave.",
				       "Advance to St. Charles Place",
				       "Advance to nearest Utility", "Advance to nearest railroad",
				       "Bank pays dividend", "Get out of Jail Free", "Go back 3 spaces",
				       "Go to Jail", "Make repairs on property", "Pay poor tax",
				       "Take trip on Reading Railroad", "Take a walk on Boardwalk",
				       "Elected Chairman of the Board", "Building loan matures",
					   "Won a crossword competition"};
	String[] CommunityCards = {"Advance to Go", "Bank error in your favor", "Doctor's fee",
            			  "Sale of stock", "Get Out of Jail Free", "Go to Jail",
            			  "Grand Opera Night", "Holiday Fund matures", "Income tax refund",
            			  "It is your birthday", "Life insurance matures", "Pay hospital fees",
            			  "Pay school fees", "Receive $25 consultancy fee",
            			  "Assessed for street repairs", "Beauty contest"};
	String[] Tiles = {"Go!", "Mediterranean Avenue", "Community Chest", "Baltic Avenue",
 		              "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance",
 		              "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Place",
 		              "Electric Company", "States Avenue", "Virginia Avenue",
 		              "Pennsylvania Railroad", "St. James Place", "Community Chest",
 		              "Tennessee Avenue", "New York Avenue", "Free Parking",
 		              "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue",
 		              "B & O Railroad", "Atlantic Avenue", "Ventnor Avenue",
 		              "Water Company", "Marvin Gardens", "Go to Jail", "Pacific Avenue",
 		              "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue",
 		              "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"};
	private String[] TileNames = {"Go!", "Mediterranean Avenue", "Baltic Avenue",
                    			  "Oriental Avenue", "Vermont Avenue", "Connecticut Avenue",
            		        	  "St. Charles Place", "States Avenue", "Virginia Avenue",
            			          "St. James Place", "Tennessee Avenue", "New York Avenue",
                                  "Kentucky Avenue", "Indiana Avenue", "Illinois Avenue",
            			          "Atlantic Avenue", "Ventnor Avenue", "Marvin Gardens",
            			          "Pacific Avenue", "North Carolina Avenue",
            			          "Pennsylvania Avenue", "Park Place", "Broadway",
            			          "Reading Railroad", "Pennsylvania Railroad",
            			          "B & O Railroad", "Short Line", "Electric Company",
            			          "Water Company", "Jail", "Free Parking", "Go to Jail",
            			          "Community Chest", "Chance", "Income Tax", "Luxury Tax"};
	private Tile[] AllTiles;
	private int P1Tile;
	private int P2Tile;
	
	public StandardBoard() {
		this.P1Tile = 0;
		this.P2Tile = 0;
		Property Mediterranean = new Property("Mediterranean Avenue", 60, 2, 30, 50, 50, 10, 30, 90, 160, 250);
		Property Baltic = new Property("Baltic Avenue", 60, 4, 30, 50, 50, 20, 60, 180, 320, 450);
		Property Oriental = new Property("Oriental Avenue", 100, 6, 50, 50, 50, 30, 90, 270, 400, 550);
		Property Vermont = new Property("Vermont Avenue", 100, 6, 50, 50, 50, 30, 90, 270, 400, 550);
		Property Connecticut = new Property("Connecticut Avenue", 120, 8, 60, 50, 50, 40, 100, 300, 450, 600);
		Property StCharles = new Property("St. Charles Place", 140, 10, 70, 100, 100, 50, 150, 450, 625, 750);
		Property States = new Property("States Avenue", 140, 10, 70, 100, 100, 50, 150, 450, 625, 750);
		Property Virginia = new Property("Virginia Avenue", 160, 12, 80, 100, 100, 60, 180, 500, 700, 900);
		Property StJames = new Property("St. James Place", 180, 14, 90, 100, 100, 70, 200, 550, 750, 950);
		Property Tennessee = new Property("Tennessee Avenue", 180, 14, 90, 100, 100, 70, 200, 550, 750, 950);
		Property NewYork = new Property("New York Avene", 200, 16, 100, 100, 100, 80, 220, 600, 800, 1000);
		Property Kentucky = new Property("Kentucky Avenue", 220, 18, 110, 150, 150, 90, 250, 700, 875, 1050);
		Property Indiana = new Property("Indiana Avenue", 220, 18, 110, 150, 150, 90, 250, 700, 875, 1050);
		Property Illinois = new Property("Illinois Avenue", 240, 20, 120, 150, 150, 100, 300, 750, 925, 1100);
		Property Atlantic = new Property("Atlantic Avenue", 260, 22, 130, 150, 150, 110, 330, 800, 975, 1150);
		Property Ventnor = new Property("Ventnor Avenue", 260, 22, 130, 150, 150, 110, 330, 800, 975, 1150);
		Property Marvin = new Property("Marvin Gardens", 280, 24, 140, 150, 150, 120, 360, 850, 1025, 1200);
		Property Pacific = new Property("Pacific Avenue", 300, 26, 150, 200, 200, 130 ,390, 900, 1100, 1275);
		Property NorthCarolina = new Property("North Carolina Avenue", 300, 26, 150, 200, 200, 130, 390, 900, 1100, 1275);
		Property PennsylvaniaP = new Property("Pennsylvania Avenue", 320, 28, 160, 200, 200, 150, 450, 1000, 1200, 1400);
		Property Park = new Property("Park Place", 350, 35, 175, 200, 200, 175, 500, 1100, 1300, 1500);
		Property Boardwalk = new Property("Boardwalk", 400, 50, 200, 200, 200, 200, 600, 1400, 1700, 2000);
		Railroad Reading = new Railroad("Reading Railroad");
		Railroad PennsylvaniaR = new Railroad("Pennsylvania Railroad");
		Railroad BnO = new Railroad("B & O Railroad");
		Railroad Short = new Railroad("Short Line");
		Utility Electric = new Utility("Electric Company");
		Utility Water = new Utility("Water Company");
		SpecialTiles Go = new SpecialTiles("Go!");
		SpecialTiles Chest = new SpecialTiles("Chest");
		SpecialTiles Income = new SpecialTiles("Income");
		SpecialTiles Chance = new SpecialTiles("Chance");
		SpecialTiles Jail = new SpecialTiles("Jail");
		SpecialTiles FreePark = new SpecialTiles("Free Parking");
		SpecialTiles GoJail = new SpecialTiles("Go to Jail");
		SpecialTiles Luxury = new SpecialTiles("Luxury Tax");
		this.AllTiles = new Tile[]{Go, Mediterranean, Chest, Baltic, Income, Reading, Oriental, Chance, Vermont,
				                   Connecticut, Jail, StCharles, Electric, States, Virginia, PennsylvaniaR,
				                   StJames, Chest, Tennessee, NewYork, FreePark, Kentucky, Chance, Indiana,
				                   Illinois, BnO, Atlantic, Ventnor, Water, Marvin, GoJail, Pacific, NorthCarolina,
				                   Chest, PennsylvaniaP, Short, Chance, Park, Luxury, Boardwalk}; 
	}
	
	public void move(Player P1, Player P2) {
		
	}
	
	
}
