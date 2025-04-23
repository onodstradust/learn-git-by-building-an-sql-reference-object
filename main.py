package com.learn-git-by-building-an-sql-reference-object

data class User(
    val id: String,
    val name: String,
    val email: String
)

class main {
    private val users = mutableListOf<User>()

    fun initialize() {
        println("Initializing learn-git-by-building-an-sql-reference-object")
        users.add(User("1", "John Doe", "john@example.com"))
        users.add(User("2", "Jane Smith", "jane@example.com"))
    }

    fun run() {
        println("Welcome to learn-git-by-building-an-sql-reference-object")
        println("Users:")
        users.forEach { user ->
            println("- \${user.name} (\${user.email})")
        }
    }

    fun addUser(user: User) {
        users.add(user)
    }

    fun getUserCount(): Int = users.size
}

fun main() {
    val app = main()
    app.initialize()
    app.run()
    println("Total users: \${app.getUserCount()}")
}

# Code Update 1760680248-24866

# Additional Implementation 1760680248

# Additional Implementation 1760680248

# Additional Implementation 1760680248

# Code Update 1760680249-7636

# Additional Implementation 1760680249

# Additional Implementation 1760680249

# Additional Implementation 1760680249

# Additional Implementation 1760680249

# Additional Implementation 1760680249

# Code Update 1760680249-25208

# Code Update 1760680249-10925

# Code Update 1760680249-29120

# Additional Implementation 1760680249

# Code Update 1760680250-29010

# Code Update 1760680250-26211

# Additional Implementation 1760680250
