# Use an official Nginx image as the base image
FROM nginx:alpine

# Copy the frontend files into the Nginx HTML directory
COPY . /usr/share/nginx/html

# Expose port 80 for the frontend
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]