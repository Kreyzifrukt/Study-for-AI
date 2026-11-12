package reposetories;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import interfaces.IStudents;
import models.Student;
//list: ArrayList, LinkedList

public class StudentsRepository implements IStudents {
	
	private final ArrayList<Student> students = new ArrayList<>();
	private final Path file = Path.of("student.txt");
	
	public StudentsRepository() {
		load();
	}

	@Override
	public void load() {
		// TODO Auto-generated method stub
		try {
			if (!Files.exists(file)) {
				System.out.println("Файл не знайдений");
				return;
			}
			List<String> fileRows = Files.readAllLines(file);
			for (String row : fileRows) {
				if (!row.isBlank()) {
					students.add(Student.fromString(row));
				}
			}
			
		}catch (IOException ex) {
			System.out.println("Помилка завантаження данних " + ex.getMessage());
		}
	}

	@Override
	public void save() {
		// TODO Auto-generated method stub
		try {
			ArrayList<String> rows = new ArrayList<>();
			for (Student s : students) {
				rows.add(s.toString());
			}
			Files.write(file, rows);
			// ->
		} catch (IOException ex) {
			System.out.println("Помилка збереження данних" + ex.getMessage());
		}
	}

	@Override
	public ArrayList<Student> findAll() {
		// 
		return students;
	}

	@Override
	public Student findById(int id) {
		for (Student s : students) {
			if (id == s.getId()) {
				return s;
			}
		}
		return null;
	}

	@Override
	public void create(Student createdstudent) {
		// TODO Auto-generated method stub
		students.add(createdStudent);
		saveData();
	}

	@Override
	public boolean update(Student updatedstudent) {
		// TODO Auto-generated method stub
		Student student = findById(updatedStudent.getId());
		if (student == null) {
			return false;
		}
		student.setName(updatedStudent.getName());
		student.setAge(updatedStudent.getAge());
		student.setRate(updatedStudent.getRate());
		return true;
	}

	@Override
	public void delete(int id) {
		// TODO Auto-generated method stub
		
	}
}
