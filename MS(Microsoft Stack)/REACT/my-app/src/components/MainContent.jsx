import React from 'react';


const course = {

}
function MainContent({selectedCourse}) {

    return (
        <>
        <main className="main-content">
            {
                selectedCourse ? (
                    <CourseCard course = {course[selectedCourse]}/>
                ):(
                    <h2>select a course to view the details</h2>
                )
            }
        </main>
        </>
    );
}

export default MainContent;