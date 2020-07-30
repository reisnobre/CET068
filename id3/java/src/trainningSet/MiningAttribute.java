package trainningSet;

import java.util.ArrayList;

public class MiningAttribute {
	
	private String name;
	private ArrayList<String> dataValues;
	
	public MiningAttribute() {
		dataValues = new ArrayList<String>();
	}

	/**
	 * This method returns true if this attribute has only one value
	 * @return
	 */
	public boolean hasOnlyOneValue() {
		String init = dataValues.get(0);
		for (String other:dataValues) {
			if (!init.equals(other))
				return false;
		}
		return true;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public ArrayList<String> getDataValues() {
		return dataValues;
	}
	
	/**
	 *This method adds a new data (from the file?)
	 *into the attribute
	 * @param data
	 */
	public void InsertData(String data) {
		dataValues.add(data);
	}

}
