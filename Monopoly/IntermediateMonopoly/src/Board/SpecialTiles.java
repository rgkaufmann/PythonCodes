package Board;

public class SpecialTiles implements Tile {
	private String name;
	
	public SpecialTiles(String name) {
		this.name = name;
	}
	
	public String getName() {
		return name;
	}
}
