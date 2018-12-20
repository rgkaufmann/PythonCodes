package Board;

public class Utility implements PropertyTile{
	private int cost;
	private int mortgage;
	private int rentmultiplier;
	private String title;
	private boolean mortgaged;
	
	public Utility(String title) {
		this.cost = 150;
		this.mortgage = 75;
		this.rentmultiplier = 4;
		this.title = title;
		this.mortgaged = false;
	}
	
	public int getCost() {
		return cost;
	}
	
	public int getRent() {
		return rentmultiplier;
	}
	
	public int getMortgage() {
		return mortgage;
	}
	
	public String getName() {
		return title;
	}
	
	public boolean getMortgaged() {
		return mortgaged;
	}
	
	public void monopolize() {
		rentmultiplier = 10;
	}
}
