// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");

int[] array = new int[5];
Console.Write("enter 5 integer values");
for (int i=0; i < 5; i++)
{
    array[i] = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine("array elements are");
for (int i=0; i <= 4; i++)
{
    Console.WriteLine(array[i]);
}
Console.WriteLine("length or size of array ", array.Length);
Array.Reverse(array);
Console.WriteLine("array reversing array elements are:");
for(int i = 0; i <= 4; i++)
{
    Console.WriteLine(array[i]);
}
Console.ReadLine();
//2d array int [,] array = new int[3,3]
