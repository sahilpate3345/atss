class SkillNormalizer:
    def __init__(self):
        # Dictionary of common skill variations -> normalized form
        self.skill_map = {
            # Python
            "python 3": "python",
            "python3": "python",
            
            # JavaScript ecosystem
            "js": "javascript",
            "reactjs": "react",
            "react.js": "react",
            "react native": "react-native",
            "nodejs": "node.js",
            "node": "node.js",
            "vuejs": "vue",
            "vue.js": "vue",
            "expressjs": "express",
            "express.js": "express",
            "nextjs": "next.js",
            "next.js": "next.js",

            # Cloud / DevOps
            "aws": "amazon web services",
            "gcp": "google cloud platform",
            "azure": "microsoft azure",
            "k8s": "kubernetes",
            "docker container": "docker",

            # Databases
            "postgres": "postgresql",
            "mongo": "mongodb",
            "ms sql": "sql server",
            "mssql": "sql server",

            # AI/ML
            "ml": "machine learning",
            "dl": "deep learning",
            "nlp": "natural language processing",
            "llm": "large language model",
            
            # Others
            "cpp": "c++",
            "dotnet": ".net",
            "c#": "c_sharp", # specialized to avoid issues matches
        }

    def normalize(self, skill_list):
        """
        Takes a list of skills and returns a normalized list.
        """
        if not skill_list:
            return []
        
        normalized = []
        for skill in skill_list:
            if not isinstance(skill, str):
                continue
            
            # Lowercase and strip
            s = skill.lower().strip()
            
            # Direct mapping
            if s in self.skill_map:
                normalized.append(self.skill_map[s])
            else:
                normalized.append(s)
                
        return normalized

# Singleton instance
normalizer = SkillNormalizer()
