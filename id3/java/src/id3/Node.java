package id3;

import java.util.ArrayList;

public class Node {
	
	private ArrayList<Node> branches;
	
	Node() {
		branches = new ArrayList<Node>();
	}
	

	/**
	 * This method returns all the banches of this node
	 * @return
	 */
	public ArrayList<Node> getBranches() {
		// TODO Auto-generated method stub
		return branches;
	}

}
