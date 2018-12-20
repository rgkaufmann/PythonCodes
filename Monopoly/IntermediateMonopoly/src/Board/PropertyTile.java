package Board;

public interface PropertyTile extends Tile{
	String getName();
	int getCost();
	int getMortgage();
	boolean getMortgaged();
	int getRent();
	void monopolize();
}
