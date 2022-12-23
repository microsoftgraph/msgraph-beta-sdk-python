from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
profile_card_annotation = lazy_import('msgraph.generated.models.profile_card_annotation')

class ProfileCardProperty(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def annotations(self,) -> Optional[List[profile_card_annotation.ProfileCardAnnotation]]:
        """
        Gets the annotations property value. Allows an administrator to set a custom display label for the directory property and localize it for the users in their tenant.
        Returns: Optional[List[profile_card_annotation.ProfileCardAnnotation]]
        """
        return self._annotations
    
    @annotations.setter
    def annotations(self,value: Optional[List[profile_card_annotation.ProfileCardAnnotation]] = None) -> None:
        """
        Sets the annotations property value. Allows an administrator to set a custom display label for the directory property and localize it for the users in their tenant.
        Args:
            value: Value to set for the annotations property.
        """
        self._annotations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new profileCardProperty and sets the default values.
        """
        super().__init__()
        # Allows an administrator to set a custom display label for the directory property and localize it for the users in their tenant.
        self._annotations: Optional[List[profile_card_annotation.ProfileCardAnnotation]] = None
        # Identifies a profileCardProperty resource in Get, Update, or Delete operations. Allows an administrator to surface hidden Azure Active Directory (Azure AD) properties on the Microsoft 365 profile card within their tenant. When present, the Azure AD field referenced in this field will be visible to all users in your tenant on the contact pane of the profile card. Allowed values for this field are: UserPrincipalName, Fax, StreetAddress, PostalCode, StateOrProvince, Alias, CustomAttribute1,  CustomAttribute2, CustomAttribute3, CustomAttribute4, CustomAttribute5, CustomAttribute6, CustomAttribute7, CustomAttribute8, CustomAttribute9, CustomAttribute10, CustomAttribute11, CustomAttribute12, CustomAttribute13, CustomAttribute14, CustomAttribute15.
        self._directory_property_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProfileCardProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProfileCardProperty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProfileCardProperty()
    
    @property
    def directory_property_name(self,) -> Optional[str]:
        """
        Gets the directoryPropertyName property value. Identifies a profileCardProperty resource in Get, Update, or Delete operations. Allows an administrator to surface hidden Azure Active Directory (Azure AD) properties on the Microsoft 365 profile card within their tenant. When present, the Azure AD field referenced in this field will be visible to all users in your tenant on the contact pane of the profile card. Allowed values for this field are: UserPrincipalName, Fax, StreetAddress, PostalCode, StateOrProvince, Alias, CustomAttribute1,  CustomAttribute2, CustomAttribute3, CustomAttribute4, CustomAttribute5, CustomAttribute6, CustomAttribute7, CustomAttribute8, CustomAttribute9, CustomAttribute10, CustomAttribute11, CustomAttribute12, CustomAttribute13, CustomAttribute14, CustomAttribute15.
        Returns: Optional[str]
        """
        return self._directory_property_name
    
    @directory_property_name.setter
    def directory_property_name(self,value: Optional[str] = None) -> None:
        """
        Sets the directoryPropertyName property value. Identifies a profileCardProperty resource in Get, Update, or Delete operations. Allows an administrator to surface hidden Azure Active Directory (Azure AD) properties on the Microsoft 365 profile card within their tenant. When present, the Azure AD field referenced in this field will be visible to all users in your tenant on the contact pane of the profile card. Allowed values for this field are: UserPrincipalName, Fax, StreetAddress, PostalCode, StateOrProvince, Alias, CustomAttribute1,  CustomAttribute2, CustomAttribute3, CustomAttribute4, CustomAttribute5, CustomAttribute6, CustomAttribute7, CustomAttribute8, CustomAttribute9, CustomAttribute10, CustomAttribute11, CustomAttribute12, CustomAttribute13, CustomAttribute14, CustomAttribute15.
        Args:
            value: Value to set for the directoryPropertyName property.
        """
        self._directory_property_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "annotations": lambda n : setattr(self, 'annotations', n.get_collection_of_object_values(profile_card_annotation.ProfileCardAnnotation)),
            "directory_property_name": lambda n : setattr(self, 'directory_property_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("annotations", self.annotations)
        writer.write_str_value("directoryPropertyName", self.directory_property_name)
    

