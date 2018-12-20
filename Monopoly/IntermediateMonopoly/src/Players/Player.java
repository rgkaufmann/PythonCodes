package Players;

import Board.PropertyTile;

public interface Player {
	public int roll();
	public boolean actionBuy(PropertyTile Tilename);
	public void actionPay(PropertyTile Tilename, Player Receiver);
	public boolean actionJail(int TurnsinJail);
}
