package trainningSet;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class TestMiningAttribute {

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testHasOnlyOneValue() {
		MiningAttribute mn = new MiningAttribute();
		mn.InsertData("Renault");
		mn.InsertData("Ferrari");
		mn.InsertData("Chevrolet");
		assertFalse(mn.hasOnlyOneValue());
		
		mn = new MiningAttribute();
		mn.InsertData("Renault");
		mn.InsertData("Renault");
		mn.InsertData("Renault");
		assertTrue(mn.hasOnlyOneValue());
		
	}

}
