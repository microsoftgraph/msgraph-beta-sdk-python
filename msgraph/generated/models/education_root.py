from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_class, education_school, education_synchronization_profile, education_user

class EducationRoot(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationRoot and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The classes property
        self._classes: Optional[List[education_class.EducationClass]] = None
        # The me property
        self._me: Optional[education_user.EducationUser] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The schools property
        self._schools: Optional[List[education_school.EducationSchool]] = None
        # The synchronizationProfiles property
        self._synchronization_profiles: Optional[List[education_synchronization_profile.EducationSynchronizationProfile]] = None
        # The users property
        self._users: Optional[List[education_user.EducationUser]] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def classes(self,) -> Optional[List[education_class.EducationClass]]:
        """
        Gets the classes property value. The classes property
        Returns: Optional[List[education_class.EducationClass]]
        """
        return self._classes
    
    @classes.setter
    def classes(self,value: Optional[List[education_class.EducationClass]] = None) -> None:
        """
        Sets the classes property value. The classes property
        Args:
            value: Value to set for the classes property.
        """
        self._classes = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_class, education_school, education_synchronization_profile, education_user

        fields: Dict[str, Callable[[Any], None]] = {
            "classes": lambda n : setattr(self, 'classes', n.get_collection_of_object_values(education_class.EducationClass)),
            "me": lambda n : setattr(self, 'me', n.get_object_value(education_user.EducationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "schools": lambda n : setattr(self, 'schools', n.get_collection_of_object_values(education_school.EducationSchool)),
            "synchronizationProfiles": lambda n : setattr(self, 'synchronization_profiles', n.get_collection_of_object_values(education_synchronization_profile.EducationSynchronizationProfile)),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(education_user.EducationUser)),
        }
        return fields
    
    @property
    def me(self,) -> Optional[education_user.EducationUser]:
        """
        Gets the me property value. The me property
        Returns: Optional[education_user.EducationUser]
        """
        return self._me
    
    @me.setter
    def me(self,value: Optional[education_user.EducationUser] = None) -> None:
        """
        Sets the me property value. The me property
        Args:
            value: Value to set for the me property.
        """
        self._me = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def schools(self,) -> Optional[List[education_school.EducationSchool]]:
        """
        Gets the schools property value. The schools property
        Returns: Optional[List[education_school.EducationSchool]]
        """
        return self._schools
    
    @schools.setter
    def schools(self,value: Optional[List[education_school.EducationSchool]] = None) -> None:
        """
        Sets the schools property value. The schools property
        Args:
            value: Value to set for the schools property.
        """
        self._schools = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("classes", self.classes)
        writer.write_object_value("me", self.me)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("schools", self.schools)
        writer.write_collection_of_object_values("synchronizationProfiles", self.synchronization_profiles)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def synchronization_profiles(self,) -> Optional[List[education_synchronization_profile.EducationSynchronizationProfile]]:
        """
        Gets the synchronizationProfiles property value. The synchronizationProfiles property
        Returns: Optional[List[education_synchronization_profile.EducationSynchronizationProfile]]
        """
        return self._synchronization_profiles
    
    @synchronization_profiles.setter
    def synchronization_profiles(self,value: Optional[List[education_synchronization_profile.EducationSynchronizationProfile]] = None) -> None:
        """
        Sets the synchronizationProfiles property value. The synchronizationProfiles property
        Args:
            value: Value to set for the synchronization_profiles property.
        """
        self._synchronization_profiles = value
    
    @property
    def users(self,) -> Optional[List[education_user.EducationUser]]:
        """
        Gets the users property value. The users property
        Returns: Optional[List[education_user.EducationUser]]
        """
        return self._users
    
    @users.setter
    def users(self,value: Optional[List[education_user.EducationUser]] = None) -> None:
        """
        Sets the users property value. The users property
        Args:
            value: Value to set for the users property.
        """
        self._users = value
    

