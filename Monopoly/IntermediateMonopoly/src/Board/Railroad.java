package Board;

public class Railroad implements PropertyTile{
	private int cost;
	private int mortgage;
	private int rent;
	private String title;
	private boolean mortgaged;
	
	public Railroad(String title) {
		this.cost = 200;
		this.mortgage = 100;
		this.rent = 25;
		this.title = title;
		this.mortgaged = false;
	}
	
	public int getCost() {
		return cost;
	}
	
	public int getRent() {
		return rent;
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
		rent += 25;
	}
}
