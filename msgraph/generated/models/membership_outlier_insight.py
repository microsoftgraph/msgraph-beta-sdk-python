from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
governance_insight = lazy_import('msgraph.generated.models.governance_insight')
outlier_container_type = lazy_import('msgraph.generated.models.outlier_container_type')
outlier_member_type = lazy_import('msgraph.generated.models.outlier_member_type')

class MembershipOutlierInsight(governance_insight.GovernanceInsight):
    def __init__(self,) -> None:
        """
        Instantiates a new MembershipOutlierInsight and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.membershipOutlierInsight"
        # Navigation link to the container directory object. For example, to a group.
        self._container: Optional[directory_object.DirectoryObject] = None
        # Indicates the identifier of the container, for example, a group ID.
        self._container_id: Optional[str] = None
        # Navigation link to a member object. For example, to a user.
        self._member: Optional[directory_object.DirectoryObject] = None
        # Indicates the identifier of the user.
        self._member_id: Optional[str] = None
        # The outlierContainerType property
        self._outlier_container_type: Optional[outlier_container_type.OutlierContainerType] = None
        # The outlierMemberType property
        self._outlier_member_type: Optional[outlier_member_type.OutlierMemberType] = None
    
    @property
    def container(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the container property value. Navigation link to the container directory object. For example, to a group.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._container
    
    @container.setter
    def container(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the container property value. Navigation link to the container directory object. For example, to a group.
        Args:
            value: Value to set for the container property.
        """
        self._container = value
    
    @property
    def container_id(self,) -> Optional[str]:
        """
        Gets the containerId property value. Indicates the identifier of the container, for example, a group ID.
        Returns: Optional[str]
        """
        return self._container_id
    
    @container_id.setter
    def container_id(self,value: Optional[str] = None) -> None:
        """
        Sets the containerId property value. Indicates the identifier of the container, for example, a group ID.
        Args:
            value: Value to set for the containerId property.
        """
        self._container_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MembershipOutlierInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MembershipOutlierInsight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MembershipOutlierInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "container": lambda n : setattr(self, 'container', n.get_object_value(directory_object.DirectoryObject)),
            "container_id": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "member": lambda n : setattr(self, 'member', n.get_object_value(directory_object.DirectoryObject)),
            "member_id": lambda n : setattr(self, 'member_id', n.get_str_value()),
            "outlier_container_type": lambda n : setattr(self, 'outlier_container_type', n.get_enum_value(outlier_container_type.OutlierContainerType)),
            "outlier_member_type": lambda n : setattr(self, 'outlier_member_type', n.get_enum_value(outlier_member_type.OutlierMemberType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def member(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the member property value. Navigation link to a member object. For example, to a user.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._member
    
    @member.setter
    def member(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the member property value. Navigation link to a member object. For example, to a user.
        Args:
            value: Value to set for the member property.
        """
        self._member = value
    
    @property
    def member_id(self,) -> Optional[str]:
        """
        Gets the memberId property value. Indicates the identifier of the user.
        Returns: Optional[str]
        """
        return self._member_id
    
    @member_id.setter
    def member_id(self,value: Optional[str] = None) -> None:
        """
        Sets the memberId property value. Indicates the identifier of the user.
        Args:
            value: Value to set for the memberId property.
        """
        self._member_id = value
    
    @property
    def outlier_container_type(self,) -> Optional[outlier_container_type.OutlierContainerType]:
        """
        Gets the outlierContainerType property value. The outlierContainerType property
        Returns: Optional[outlier_container_type.OutlierContainerType]
        """
        return self._outlier_container_type
    
    @outlier_container_type.setter
    def outlier_container_type(self,value: Optional[outlier_container_type.OutlierContainerType] = None) -> None:
        """
        Sets the outlierContainerType property value. The outlierContainerType property
        Args:
            value: Value to set for the outlierContainerType property.
        """
        self._outlier_container_type = value
    
    @property
    def outlier_member_type(self,) -> Optional[outlier_member_type.OutlierMemberType]:
        """
        Gets the outlierMemberType property value. The outlierMemberType property
        Returns: Optional[outlier_member_type.OutlierMemberType]
        """
        return self._outlier_member_type
    
    @outlier_member_type.setter
    def outlier_member_type(self,value: Optional[outlier_member_type.OutlierMemberType] = None) -> None:
        """
        Sets the outlierMemberType property value. The outlierMemberType property
        Args:
            value: Value to set for the outlierMemberType property.
        """
        self._outlier_member_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("container", self.container)
        writer.write_str_value("containerId", self.container_id)
        writer.write_object_value("member", self.member)
        writer.write_str_value("memberId", self.member_id)
        writer.write_enum_value("outlierContainerType", self.outlier_container_type)
        writer.write_enum_value("outlierMemberType", self.outlier_member_type)
    

