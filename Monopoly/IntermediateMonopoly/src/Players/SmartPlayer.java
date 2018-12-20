package Players;

import Board.PropertyTile;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class SmartPlayer implements Player {
	
	private String[] ChoiceProperties;
	private int money;
	private List<PropertyTile> Purchases;
	
	public SmartPlayer() {
		this.money = 1500;
		this.Purchases = new ArrayList<PropertyTile>();
		this.ChoiceProperties = new String[] {"New York Avenue", "Tennessee Avenue", "St. James Place", "Illinois Avenue",
											  "Kentucky Avenue", "Indiana Avenue", "Atlantic Avenue", "Ventnor Avenue",
											  "Marvin Gardens", "Reading Railroad", "Pennsylvania Railroad", "B & O Railroad",
											  "Short Line", "St. Charles Place", "Stats Avenue", "Virginia Avenue",
											  "Pacific Avenue", "North Carolina Avenue", "Pennsylvania Avenue", "Water Company",
											  "Electric Company", "Vermont Avenue", "Connecticut Avenue", "Oriental Avenue",
											  "Mediterranean Avenue", "Baltic Avenue", "Boardwalk", "Park Place"};
	}
	
	public int roll() {
		Random dice = new Random();
		int diceroll = dice.nextInt(6)+1;
		diceroll += dice.nextInt(6) + 1;
		return diceroll;
	}
	
	public boolean actionBuy(PropertyTile givenTile) {
		for (String ChoiceProperty: Arrays.copyOfRange(ChoiceProperties, 0, 5)) {
			if (givenTile.getName().equalsIgnoreCase(ChoiceProperty) && money>givenTile.getCost()){
				money -= givenTile.getCost();
				Purchases.add(givenTile);
				return true;
			}
		}
		return false;
	}
	
	public void actionPay(PropertyTile givenTile, Player Receiver) {
		
	}
	
	public boolean actionJail(int TurnsinJail) {
		return false;
	}
}
