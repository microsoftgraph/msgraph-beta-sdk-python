from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class MicrosoftApplicationDataAccessSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftApplicationDataAccessSettings and sets the default values.
        """
        super().__init__()
        # The ID of an Azure Active Directory (Azure AD) security group for which the members are allowed to access Microsoft 365 data using only Microsoft 365 apps, but not other Microsoft apps such as Edge.  This is only applicable if isEnabledForAllMicrosoftApplications is set to true.
        self._disabled_for_group: Optional[str] = None
        # When set to true, all users in the organization can access in a Microsoft app any Microsoft 365 data that the user has been authorized to access. The Microsoft app can be a Microsoft 365 app (for example, Excel, Outlook) or non-Microsoft 365 app (for example, Edge). The default is true.  It is possible to disable this access for a subset of users in an Azure AD security group, by specifying the group in the disabledForGroup property.  When set to false, all users can access authorized Microsoft 365 data only in a Microsoft 365 app.
        self._is_enabled_for_all_microsoft_applications: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftApplicationDataAccessSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftApplicationDataAccessSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftApplicationDataAccessSettings()
    
    @property
    def disabled_for_group(self,) -> Optional[str]:
        """
        Gets the disabledForGroup property value. The ID of an Azure Active Directory (Azure AD) security group for which the members are allowed to access Microsoft 365 data using only Microsoft 365 apps, but not other Microsoft apps such as Edge.  This is only applicable if isEnabledForAllMicrosoftApplications is set to true.
        Returns: Optional[str]
        """
        return self._disabled_for_group
    
    @disabled_for_group.setter
    def disabled_for_group(self,value: Optional[str] = None) -> None:
        """
        Sets the disabledForGroup property value. The ID of an Azure Active Directory (Azure AD) security group for which the members are allowed to access Microsoft 365 data using only Microsoft 365 apps, but not other Microsoft apps such as Edge.  This is only applicable if isEnabledForAllMicrosoftApplications is set to true.
        Args:
            value: Value to set for the disabledForGroup property.
        """
        self._disabled_for_group = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "disabled_for_group": lambda n : setattr(self, 'disabled_for_group', n.get_str_value()),
            "is_enabled_for_all_microsoft_applications": lambda n : setattr(self, 'is_enabled_for_all_microsoft_applications', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled_for_all_microsoft_applications(self,) -> Optional[bool]:
        """
        Gets the isEnabledForAllMicrosoftApplications property value. When set to true, all users in the organization can access in a Microsoft app any Microsoft 365 data that the user has been authorized to access. The Microsoft app can be a Microsoft 365 app (for example, Excel, Outlook) or non-Microsoft 365 app (for example, Edge). The default is true.  It is possible to disable this access for a subset of users in an Azure AD security group, by specifying the group in the disabledForGroup property.  When set to false, all users can access authorized Microsoft 365 data only in a Microsoft 365 app.
        Returns: Optional[bool]
        """
        return self._is_enabled_for_all_microsoft_applications
    
    @is_enabled_for_all_microsoft_applications.setter
    def is_enabled_for_all_microsoft_applications(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabledForAllMicrosoftApplications property value. When set to true, all users in the organization can access in a Microsoft app any Microsoft 365 data that the user has been authorized to access. The Microsoft app can be a Microsoft 365 app (for example, Excel, Outlook) or non-Microsoft 365 app (for example, Edge). The default is true.  It is possible to disable this access for a subset of users in an Azure AD security group, by specifying the group in the disabledForGroup property.  When set to false, all users can access authorized Microsoft 365 data only in a Microsoft 365 app.
        Args:
            value: Value to set for the isEnabledForAllMicrosoftApplications property.
        """
        self._is_enabled_for_all_microsoft_applications = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("disabledForGroup", self.disabled_for_group)
        writer.write_bool_value("isEnabledForAllMicrosoftApplications", self.is_enabled_for_all_microsoft_applications)
    

