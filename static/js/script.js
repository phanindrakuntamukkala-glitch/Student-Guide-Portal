/* General */

body{
    margin:0;
    font-family:Arial, Helvetica, sans-serif;
    background:#f5f7fb;
}

/* Dashboard Layout */

.dashboard-container{
    display:flex;
    gap:25px;
    padding:20px;
}

/* Profile Card */

.profile-card{
    width:350px;
    background:#0d6efd;
    color:white;
    border-radius:15px;
    overflow:hidden;
}

.profile-img{
    width:140px;
    height:140px;
    border-radius:50%;
    margin:20px auto;
    display:block;
    object-fit:cover;
}

/* Main Content */

.main-content{
    flex:1;
}

/* Search Bar */

.search-container{
    display:flex;
    gap:15px;
    margin-bottom:25px;
}

.search-box{
    flex:1;
    padding:14px;
    border:none;
    border-radius:10px;
}

.search-btn{
    background:#2563eb;
    color:white;
    border:none;
    padding:14px 25px;
    border-radius:10px;
}

/* Top Cards */

.top-cards{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
}

.info-card{
    background:white;
    border-radius:15px;
    padding:20px;
    text-align:center;
    box-shadow:0 10px 20px rgba(0,0,0,.08);
}
.dashboard-card{
    width:95%;
    margin:30px auto;
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 10px 20px rgba(0,0,0,.1);
}

.timetable{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

.timetable th{
    background:#2563eb;
    color:white;
    padding:15px;
}

.timetable td{
    border:1px solid #ddd;
    padding:12px;
    text-align:center;
}

.timetable tr:nth-child(even){
    background:#f8f9fa;
}

.info-card{
    cursor:pointer;
    transition:0.3s;
}

.info-card:hover{
    transform:translateY(-5px);
}