from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class UserPrintUsageSummary(AdditionalDataHolder, Parsable):
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
    def completed_job_count(self,) -> Optional[int]:
        """
        Gets the completedJobCount property value. The completedJobCount property
        Returns: Optional[int]
        """
        return self._completed_job_count
    
    @completed_job_count.setter
    def completed_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completedJobCount property value. The completedJobCount property
        Args:
            value: Value to set for the completedJobCount property.
        """
        self._completed_job_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userPrintUsageSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The completedJobCount property
        self._completed_job_count: Optional[int] = None
        # The incompleteJobCount property
        self._incomplete_job_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The user property
        self._user: Optional[identity.Identity] = None
        # The userDisplayName property
        self._user_display_name: Optional[str] = None
        # The userPrincipalName property
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserPrintUsageSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserPrintUsageSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserPrintUsageSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_job_count": lambda n : setattr(self, 'completed_job_count', n.get_int_value()),
            "incomplete_job_count": lambda n : setattr(self, 'incomplete_job_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(identity.Identity)),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def incomplete_job_count(self,) -> Optional[int]:
        """
        Gets the incompleteJobCount property value. The incompleteJobCount property
        Returns: Optional[int]
        """
        return self._incomplete_job_count
    
    @incomplete_job_count.setter
    def incomplete_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the incompleteJobCount property value. The incompleteJobCount property
        Args:
            value: Value to set for the incompleteJobCount property.
        """
        self._incomplete_job_count = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("completedJobCount", self.completed_job_count)
        writer.write_int_value("incompleteJobCount", self.incomplete_job_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user(self,) -> Optional[identity.Identity]:
        """
        Gets the user property value. The user property
        Returns: Optional[identity.Identity]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the user property value. The user property
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. The userDisplayName property
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. The userDisplayName property
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The userPrincipalName property
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The userPrincipalName property
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

