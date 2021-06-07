using System;

public class Dog
{
	public string Name;
	public int Age;
	public List<string> Owners;
	public List<string> Tricks;

	public Dog(string Name, int Age, List<string> Owners)
	{
		this.Name = Name;
		this.Age = Age;
		this.Owners = Owners;
		this.Tricks = new List<string>();
	}

	public void Learn(string Trick)
    {
		this.Tricks.add(Trick);
    }

	public void Compare(Dog dog)
    {
		foreach (string trick in Tricks)
        {
			if (dog.Tricks.Contains(trick))
            {
				Console.WriteLine(trick);
            }
        }
    }
}
