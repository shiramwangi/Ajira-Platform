// Dashboard.jsx
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"
import { Home, Users, Settings, LogOut } from "lucide-react"

const data = [
  { name: "Mon", users: 40 },
  { name: "Tue", users: 80 },
  { name: "Wed", users: 60 },
  { name: "Thu", users: 100 },
  { name: "Fri", users: 75 },
  { name: "Sat", users: 50 },
  { name: "Sun", users: 90 },
]

export default function Dashboard() {
  return (
    <div className="flex min-h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-white shadow-lg flex flex-col p-4">
        <h2 className="text-2xl font-bold mb-6">MyApp</h2>
        <nav className="flex flex-col gap-4">
          <Button variant="ghost" className="flex gap-2 items-center">
            <Home size={18} /> Dashboard
          </Button>
          <Button variant="ghost" className="flex gap-2 items-center">
            <Users size={18} /> Users
          </Button>
          <Button variant="ghost" className="flex gap-2 items-center">
            <Settings size={18} /> Settings
          </Button>
        </nav>
        <div className="mt-auto">
          <Button variant="destructive" className="flex gap-2 items-center">
            <LogOut size={18} /> Logout
          </Button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6">
        {/* Header */}
        <header className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-semibold">Dashboard</h1>
          <Button>+ Add New</Button>
        </header>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <Card className="rounded-2xl shadow">
            <CardContent className="p-4">
              <h2 className="text-gray-500">Total Users</h2>
              <p className="text-2xl font-bold">1,245</p>
            </CardContent>
          </Card>
          <Card className="rounded-2xl shadow">
            <CardContent className="p-4">
              <h2 className="text-gray-500">Active Sessions</h2>
              <p className="text-2xl font-bold">312</p>
            </CardContent>
          </Card>
          <Card className="rounded-2xl shadow">
            <CardContent className="p-4">
              <h2 className="text-gray-500">Revenue</h2>
              <p className="text-2xl font-bold">$4,560</p>
            </CardContent>
          </Card>
        </div>

        {/* Chart Section */}
        <Card className="rounded-2xl shadow">
          <CardContent className="p-6">
            <h2 className="text-lg font-semibold mb-4">User Growth</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="users" fill="#3b82f6" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </main>
    </div>
  )
}

