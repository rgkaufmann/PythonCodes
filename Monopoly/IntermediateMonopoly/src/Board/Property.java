package Board;

public class Property implements PropertyTile{
	private int cost;
	private int mortgage;
	private int rent;
	private int housecost;
	private int hotelcost;
	private boolean buyhouses;
	private boolean buyhotels;
	private int rent1house;
	private int rent2house;
	private int rent3house;
	private int rent4house;
	private int renthotel;
	private int housenum;
	private int hotelnum;
	private String title;
	private boolean mortgaged;
	
	public Property(String title, int cost, int rent, int mortgage, int housecost,
			        int hotelcost, int rent1house, int rent2house, int rent3house,
			        int rent4house, int renthotel) {
		this.cost = cost;
		this.mortgage = mortgage;
		this.rent = rent;
		this.housecost = housecost;
		this.hotelcost = hotelcost;
		this.buyhouses = false;
		this.buyhotels = false;
		this.housenum = 0;
		this.hotelnum = 0;
		this.rent1house = rent1house;
		this.rent2house = rent2house;
		this.rent3house = rent3house;
		this.rent4house = rent4house;
		this.renthotel = renthotel;
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
	
	public int getHouseCost() {
		return housecost;
	}
	
	public int getHotelCost() {
		return hotelcost;
	}
	
	public boolean getBuyHouses() {
		return buyhouses;
	}
	
	public boolean getBuyHotels() {
		return buyhotels;
	}
	
	public int getHouseNum() {
		return housenum;
	}
	
	public int getHotelNum() {
		return hotelnum;
	}
	
	public String getName() {
		return title;
	}
	
	public boolean getMortgaged() {
		return mortgaged;
	}
	
	public void monopolize() {
		this.buyhouses = true;
		this.rent = 2*this.rent;
	}
	
	public boolean buyHouse() {
		if (buyhouses) {
			if (housenum==0) {
				housenum++;
				rent = rent1house;
				return true;
			}
			else if (housenum==1) {
				housenum++;
				rent = rent2house;
				return true;
			}
			else if (housenum==2) {
				housenum++;
				rent = rent3house;
				return true;
			}
			else if (housenum==3) {
				housenum++;
				rent = rent4house;
				buyhouses = false;
				buyhotels = true;
				return false;
			}
		}
		return false;
	}
	
	public boolean buyHotel() {
		if (buyhotels) {
			housenum = 0;
			hotelnum = 1;
			buyhotels = false;
			rent = renthotel;
			return true;
		}
		return false;
	}
}
