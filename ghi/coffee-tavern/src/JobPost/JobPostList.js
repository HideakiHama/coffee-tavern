import * as React from 'react';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import {useState, useEffect} from "react"

const theme = createTheme();

export default function JobPostList() {
  const [jobForm, setJobForm] = useState([]);

  useEffect(() => {
    const getJobForm = async () => {
      const response = await fetch("http://localhost:8000/get_all_form");
      const data = await response.json();
      console.log("DATA", data)
      setJobForm(data)
    }
    getJobForm()
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <main>
      {/* <div style={{backgroundImage: `URL(https://www.setaswall.com/wp-content/uploads/2017/07/Coffee-Background-45-2560x1600-768x480.jpg)`}}>
        Hello World
      </div> */}
        {/* Hero unit */}
        <Container sx={{ py: 8 }} maxWidth="md">
          {/* End hero unit */}
          <Grid container spacing={4}>
            {jobForm.map((jobForms) => (
              <Grid item  xs={12} sm={6} md={4}>
                  <Card
                  sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
                  key={jobForms.id}>
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="h5" component="h2">
                      {jobForms.employer}
                    </Typography>
                    <Typography>
                      {jobForms.description}
                    </Typography>
                    <Typography>
                      {jobForms.position}
                    </Typography>
                  </CardContent>
                  <CardActions>
                    <Button size="small">View</Button>
                  </CardActions>
                </Card>
              </Grid>
                ))}
          </Grid>
        </Container>
      </main>
      {/* Footer */}
      {/* <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
        <Typography variant="h6" align="center" gutterBottom>
          Footer
        </Typography>
        <Typography
          variant="subtitle1"
          align="center"
          color="text.secondary"
          component="p"
        >
          Something here to give the footer a purpose!
        </Typography>
      </Box> */}
      {/* End footer */}
    </ThemeProvider>
  );
}