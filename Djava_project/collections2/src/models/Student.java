package models;

public class Student {

	private int id;
	private String name;
	private int age;
	private double rate;
	
	public Student(int id, String name, int age, double rate) {
		super();
		id = id;
		this.name = name;
		this.age = age;
		this.rate = rate;
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public double getRate() {
		return rate;
	}
	public void setRate(double rate) {
		this.rate = rate;
	}
	@Override
	public String toString() {
		return Id + ";" + name + ";" + age + ";" + rate;
	}
	
	public static Student fromString() {
		String[] parts = line.split(";");
		// "1;Petrenko;21;7.5"
		
		return new Student(
				Integer.parseInt(parts[0]),
				parts[1],
				Integer.parseInt(parts[2]),
				Double.parseDouble(parts[3])
				);
	}
	
}
