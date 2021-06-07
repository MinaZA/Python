using System;

public class HeroPrg
{
    public string name;
    public int Atk;
    public int Def;
    public int Pv;

    public HeroPrg(string Name,string role)
    {
        this.name = Name;

        if (role == "Warrior")
        {
            this.Atk = 100;
            this.Def = 2;
            this.Pv = 10;
        }
        else if (role == "Mage")
        {
            this.Atk = 200;
            this.Def = 5;
            this.Pv = 8;
        }
    }

    public void Damage(int dmg)
    {
        dmg -= this.Def;
        this.Pv -= dmg;
    }
}