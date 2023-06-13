from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, governance_insight, outlier_container_type, outlier_member_type, user

from . import governance_insight

@dataclass
class MembershipOutlierInsight(governance_insight.GovernanceInsight):
    odata_type = "#microsoft.graph.membershipOutlierInsight"
    # Navigation link to the container directory object. For example, to a group.
    container: Optional[directory_object.DirectoryObject] = None
    # Indicates the identifier of the container, for example, a group ID.
    container_id: Optional[str] = None
    # Navigation link to a member object who modified the record. For example, to a user.
    last_modified_by: Optional[user.User] = None
    # Navigation link to a member object. For example, to a user.
    member: Optional[directory_object.DirectoryObject] = None
    # Indicates the identifier of the user.
    member_id: Optional[str] = None
    # The outlierContainerType property
    outlier_container_type: Optional[outlier_container_type.OutlierContainerType] = None
    # The outlierMemberType property
    outlier_member_type: Optional[outlier_member_type.OutlierMemberType] = None
    
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
        from . import directory_object, governance_insight, outlier_container_type, outlier_member_type, user

        fields: Dict[str, Callable[[Any], None]] = {
            "container": lambda n : setattr(self, 'container', n.get_object_value(directory_object.DirectoryObject)),
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(user.User)),
            "member": lambda n : setattr(self, 'member', n.get_object_value(directory_object.DirectoryObject)),
            "memberId": lambda n : setattr(self, 'member_id', n.get_str_value()),
            "outlierContainerType": lambda n : setattr(self, 'outlier_container_type', n.get_enum_value(outlier_container_type.OutlierContainerType)),
            "outlierMemberType": lambda n : setattr(self, 'outlier_member_type', n.get_enum_value(outlier_member_type.OutlierMemberType)),
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
        writer.write_object_value("container", self.container)
        writer.write_str_value("containerId", self.container_id)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_object_value("member", self.member)
        writer.write_str_value("memberId", self.member_id)
        writer.write_enum_value("outlierContainerType", self.outlier_container_type)
        writer.write_enum_value("outlierMemberType", self.outlier_member_type)
    

