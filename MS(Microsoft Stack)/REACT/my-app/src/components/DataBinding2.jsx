const DataBinding2 = () =>{
    const courseTable = [
      { id: 1, name: "python", duration: "2 months", price: "23444" },
      { id: 2, name: "data science", duration: "3 months", price: "3244" },
      { id: 3, name: "azure", duration: "2 months", price: "2343423" },
      { id: 4, name: "aws", duration: "3 months", price: "2432" },
      { id: 5, name: "kubernetes", duration: "2 months", price: "345634" },
    ];

    return (
        <>
        <div>
            <table border="1px">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>name</th>
                        <th>duration</th>
                        <th>price</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        courseTable.map((course)=>(
                            <tr key={course.id}>
                                <td>{course.id}</td>
                                <td>{course.name}</td>
                                <td>{course.duration}</td>
                                <td>{course.price}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
        </>
    )
}

export default DataBinding2