using System;

public class Dog
{
	public string Name;
	public int Age;
	public List<string> Owners;
	public List<string> Tricks;


	public Dog(string Name,int Age,string Owners)
	{
		this.Name = Name;
		this.Age = Age;
		this.Owners = Owners;
		Tricks = new List<string>();
	}

	public void Learn(string trick)
    {
		this.Tricks.Add(trick);
    }
}
