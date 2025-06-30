# GitHub Setup Guide for PDF Merger Tool

This guide will help you set up the PDF Merger Tool project on GitHub with proper CI/CD, issue templates, and documentation.

## Prerequisites

- GitHub account
- Git installed locally
- Python 3.6+ installed

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Name the repository: `PDF-Merger`
4. Make it **Public** (for open source)
5. **Don't** initialize with README, .gitignore, or license (we'll add these)
6. Click "Create repository"

## Step 2: Update Configuration Files

Before pushing to GitHub, update these files:

- `README.md` - Replace `siva4it` with your actual GitHub username
- `setup.py` - Update URLs and metadata
- `pyproject.toml` - Update project URLs
- `src/pdf_merger/__init__.py` - Update package metadata

## Step 3: Initialize Local Repository

```bash
# Initialize git repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: PDF Merger Tool v1.0.0 - Professional Python package for merging multiple PDF files"

# Add remote origin
git remote add origin https://github.com/siva4it/PDF-Merger.git

# Rename default branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 4: Verify GitHub Actions

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. You should see the workflow running automatically
4. Wait for it to complete successfully

## Step 5: Enable GitHub Features

### Issues
- Go to Settings → Features
- Ensure "Issues" is enabled
- The issue templates will be automatically available

### Pull Requests
- Pull requests are enabled by default
- The PR template will be automatically used

### Pages (Optional)
- Go to Settings → Pages
- Source: "Deploy from a branch"
- Branch: `main` → `/docs`
- Save

## Step 6: Update Repository Settings

### Description
Add a description: "Professional Python tool for merging multiple PDF files with advanced features"

### Topics
Add relevant topics:
- pdf
- merge
- python
- utility
- document-processing
- pypdf2

### Social Preview
Upload a custom image for social media sharing

## Step 7: Create Releases

### First Release
1. Go to "Releases" in your repository
2. Click "Create a new release"
3. Tag: `v1.0.0`
4. Title: "PDF Merger Tool v1.0.0"
5. Description: Use the content from `CHANGELOG.md`
6. Publish release

## Step 8: Documentation

### Update README
- Ensure all badges are working
- Update installation instructions
- Add usage examples

### Wiki (Optional)
- Create a wiki for detailed documentation
- Add troubleshooting guides
- Include advanced usage examples

## Step 9: Community Guidelines

### Code of Conduct
Consider adding a Code of Conduct file:
- Go to Settings → General → Code of Conduct
- Choose a template and add it

### Contributing Guidelines
The `CONTRIBUTING.md` file is already included and will be automatically linked.

## Step 10: Security

### Security Policy
1. Go to Settings → Security & analysis
2. Enable "Security advisories"
3. Create a security policy file

### Dependabot
1. Go to Settings → Security & analysis
2. Enable "Dependency graph"
3. Enable "Dependabot alerts"
4. Enable "Dependabot security updates"

## Troubleshooting

### GitHub Actions Failures
- Check the Actions tab for error details
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Import Errors
- Make sure the package structure is correct
- Check that `__init__.py` files exist
- Verify import paths in tests

### Build Errors
- Check `setup.py` syntax
- Verify `pyproject.toml` configuration
- Ensure all required files exist

## Next Steps

1. **Update URLs**: Remember to replace `siva4it` with your actual GitHub username
2. **Add collaborators**: Invite contributors to your repository
3. **Create issues**: Add some initial issues for future development
4. **Share**: Promote your project on social media and developer communities

## Maintenance

### Regular Tasks
- Monitor GitHub Actions for failures
- Review and merge pull requests
- Update dependencies regularly
- Respond to issues promptly

### Version Updates
- Update version numbers in multiple files:
  - `setup.py`
  - `pyproject.toml`
  - `src/pdf_merger/__init__.py`
  - `CHANGELOG.md`

### Documentation Updates
- Keep README.md current
- Update examples as features change
- Maintain changelog for all releases

Your PDF Merger Tool is now professionally set up on GitHub with CI/CD, proper documentation, and community features! 