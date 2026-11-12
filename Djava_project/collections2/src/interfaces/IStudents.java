package interfaces;

import java.util.ArrayList;
import models.Student;
public interface IStudents {
	// Base:
	void load();
	void save();
	
	//Crud
	ArrayList<Student> findAll();
	Student findById(int id);
	void create(Student createdstudent);
	boolean update(Student updatedstudent);
	void delete(int id);
}
